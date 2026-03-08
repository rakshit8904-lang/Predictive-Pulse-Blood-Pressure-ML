from django.shortcuts import render
from .forms import BPForm
from .ml_model import predict_bp


stage_map = {
0: "Normal Blood Pressure",
1: "Stage 1 Hypertension",
2: "Stage 2 Hypertension",
3: "Hypertensive Crisis"
}

color_map = {
0: "#10b981",
1: "#f59e0b",
2: "#f97316",
3: "#ef4444"
}

recommendations = {

0: [
"Maintain healthy lifestyle",
"Regular physical activity",
"Balanced low sodium diet",
"Annual blood pressure monitoring"
],

1: [
"Schedule appointment with healthcare provider",
"Implement DASH diet plan",
"Increase physical activity gradually",
"Monitor BP weekly"
],

2: [
"Consult physician within 1-2 days",
"Likely medication therapy required",
"Daily blood pressure monitoring",
"Reduce sodium intake"
],

3: [
"Seek emergency medical attention",
"Call emergency services if symptoms worsen",
"Do not delay treatment"
]

}


def dashboard(request):

    form = BPForm()
    result_text = None
    result_color = None
    result_recommendation = None
    confidence = None

    if request.method == "POST":

        form = BPForm(request.POST)

        if form.is_valid():

            data = [

                form.cleaned_data['gender'],
                form.cleaned_data['age'],
                form.cleaned_data['history'],
                form.cleaned_data['patient'],
                form.cleaned_data['medication'],
                form.cleaned_data['severity'],
                form.cleaned_data['breath'],
                form.cleaned_data['visual'],
                form.cleaned_data['nose'],
                form.cleaned_data['diagnosed'],
                form.cleaned_data['systolic'],
                form.cleaned_data['diastolic'],
                form.cleaned_data['diet']

            ]

            prediction = predict_bp(data)

            result_text = stage_map[prediction]
            result_color = color_map[prediction]
            result_recommendation = recommendations[prediction]

            confidence = 87.5

    return render(request,'index.html',{
        'form':form,
        'result_text':result_text,
        'result_color':result_color,
        'recommendation':result_recommendation,
        'confidence':confidence
    })