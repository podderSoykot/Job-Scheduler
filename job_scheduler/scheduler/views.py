from django.shortcuts import render
from .models import Job
import bisect


def job_scheduling():
    jobs = list(Job.objects.all().order_by('end_time'))  
    n = len(jobs)
    
    
    dp = [0] * (n + 1)
    job_ends = [job.end_time for job in jobs]  

    for i in range(1, n + 1):
        job = jobs[i - 1]
     
        idx = bisect.bisect_right(job_ends, job.start_time) - 1
        dp[i] = max(dp[i - 1], job.profit + (dp[idx + 1] if idx != -1 else 0))

    return dp[-1]

def home(request):
    max_profit = job_scheduling()
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs, 'max_profit': max_profit})

