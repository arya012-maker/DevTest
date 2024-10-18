import pandas as pd
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FileUploadForm
import os

def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            
            
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            elif uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(file_path)
            
          
            summary_report = df.groupby(['Cust State', 'Cust Pin']).agg({'DPD': 'sum'}).reset_index()

            return render(request, 'summary.html', {'summary_report': summary_report.to_html()})
    else:
        form = FileUploadForm()
    
    return render(request, 'upload.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
