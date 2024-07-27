from flask import Flask, jsonify, redirect, render_template, request
import joblib
import pandas as pd
from .team import teams

app = Flask(__name__, template_folder="templates")

# models
formation_encoder = joblib.load("../PRE-PREDICT/formation_ohe.pkl")
team_label_encoder = joblib.load("../PRE-PREDICT/team_label_encoder.pkl")
attendence_scaler = joblib.load("../PRE-PREDICT/scaler_for_attendence.pkl")
model = joblib.load("../PRE-PREDICT/model-gbs.pkl")

predict_args = {
    "1": "Win",
    "0": "lose/Draw",
}
venue = {"home": 1, "away": 0}
formation_cols = formation_encoder.get_feature_names_out()


@app.route("/")
def home():
    return redirect("/predict")


@app.route("/predict/", methods=["GET", "POST"])
def predict():
    context = {"teams": teams}
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        data = {
            "Time": request_data["time"],
            "venue_code": venue[request_data["venue"]],
            "match_week": request_data["match_week"],
            "opponent_encoded": team_label_encoder.transform(
                [[request_data["opponent"].lower()]][0]
            ),
            "team_encoded": team_label_encoder.transform(
                [[request_data["team"].lower()]][0]
            ),
        }
        datadf = pd.DataFrame([data])
        # print(datadf.shape)

        attendence_scaled = attendence_scaler.transform([[request_data["attendance"]]])[
            0
        ]
        attendence_df = pd.DataFrame(attendence_scaled, columns=["Attendance"])

        formation = formation_encoder.transform([[request_data["formation"]]])
        formation_df = pd.DataFrame(formation, columns=formation_cols)

        # print(formation_df.shape)
        final_df = pd.concat([datadf, formation_df, attendence_df], axis=1).astype(
            "float"
        )

        # print(final_df.shape)
        # print(final_df.dtypes)
        prediction = model.predict(final_df)
        context = {
            "prediction": str(prediction[0]),
            "teamA": request_data["team"],
            "teamB": request_data["opponent"],
            "teamA_image": f"../static/images/{request_data['team'].lower()}.jpg",
            "teamB_image": f"../static/images/{request_data['opponent'].lower()}.jpg",
        }

        return render_template("index.html", context=context)

    return render_template("index.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
