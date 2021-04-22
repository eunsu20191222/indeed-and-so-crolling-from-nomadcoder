from indeed import get_jobs as iget_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

so_jobs = get_so_jobs()
indeed_jobs = iget_jobs()
jobs =  so_jobs + indeed_jobs 
save_to_file(jobs)
