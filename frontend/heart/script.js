let currentStep = 1;

function calcBMI() {
    const h = document.getElementById('Height').value;
    const w = document.getElementById('Weight').value;
    if (h > 0 && w > 0) {
        document.getElementById('bmiDisplay').innerText = (w / ((h / 100) ** 2)).toFixed(1);
    }
}

function nextStep(step) {
    const isGoingForward = step > currentStep;

    if (isGoingForward) {
        const currentStepElement = document.getElementById(`step${currentStep}`);
        const currentFields = currentStepElement.querySelectorAll('input, select');
        
        for (let field of currentFields) {
            if (field.hasAttribute('required') && !field.value) {
                alert("لطفاً همه فیلدها را در این مرحله پر کنید.");
                return; 
            }
        }
    }

    document.getElementById(`step${currentStep}`).style.display = 'none';

    currentStep = step;
    document.getElementById(`step${currentStep}`).style.display = 'block';
    
    const progressPercent = (currentStep / 3) * 100; 
    document.getElementById('progressBar').style.width = progressPercent + "%";
    
    document.querySelectorAll('.steps-labels span').forEach((span, index) => {
        if (index + 1 <= currentStep) {
            span.classList.add('active');
        } else {
            span.classList.remove('active');
        }
    });
}


function resetForm() {
    document.getElementById('healthForm').reset();

    document.getElementById('bmiDisplay').innerText = "0";

    document.getElementById('resultCard').style.display = 'none';
    document.getElementById('formCard').style.display = 'block';

    currentStep = 1;

    document.getElementById('progressBar').style.width = "33.3%";
    document.querySelectorAll('.steps-labels span').forEach((s, i) => {
        s.classList.toggle('active', i === 0);
    });

    document.querySelectorAll('.step').forEach(step => step.style.display = 'none');
    document.getElementById('step1').style.display = 'block';
}

document.getElementById('healthForm').onsubmit = function(e) {
    e.preventDefault();
    
    const rawData = {
        "Age": document.getElementById('Age').value,
        "Gender": document.getElementById('Gender').value,
        "Height": document.getElementById('Height').value,
        "Weight": document.getElementById('Weight').value,
        "BMI": document.getElementById('bmiDisplay').innerText,
        "BloodPressure": document.getElementById('BloodPressure').value,
        "Cholesterol": document.getElementById('Cholesterol').value,
        "HeartRate": document.getElementById('HeartRate').value,
        "Smoking": document.getElementById('smoking').value,
        "ExerciseHours": document.getElementById('ExerciseHours').value,
        "FamilyHistory": document.getElementById('familyHistory').value
    };

    const displayLabels = {
        "Age": "سن",
        "Gender": "جنسیت",
        "Height": "قد (سانتی‌متر)",
        "Weight": "وزن (کیلوگرم)",
        "BMI": "شاخص توده بدنی (BMI)",
        "BloodPressure": "فشار خون",
        "Cholesterol": "کلسترول",
        "HeartRate": "ضربان قلب",
        "Smoking": "وضعیت مصرف سیگار",
        "ExerciseHours": "ساعت ورزش در هفته",
        "FamilyHistory": "سابقه خانوادگی"
    };

    document.getElementById('formCard').style.display = 'none';
    document.getElementById('resultCard').style.display = 'block';
    
    let html = "";
    for(let key in rawData) {
        let value = rawData[key];
        let label = displayLabels[key];

        if (key === "Gender") {
            value = (value === "Male") ? "مرد" : "زن";
        }
 
        else if (key === "Smoking") {
            value = (value === "1") ? "سیگاری" : "غیر سیگاری";
        }

        else if (key === "FamilyHistory") {
            value = (value === "1") ? "دارد" : "ندارد";
        }

        html += `<p><strong style="color: #333;">${label}:</strong> ${value}</p>`;
    }
    
    document.getElementById('summaryContent').innerHTML = html;
    

    document.getElementById('apiResult').innerText = "نتیجه مدل: احتمال خطر پایین (نرمال)";
};
