# Given N jobs where every job is represented by start_time,end_time,profit.

class Job:
    def __init__(self,id,start_time,end_time,profit):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.profit = profit

def maxProfit(jobs):
    cache = [0 for _ in range(len(jobs))]
    cache[0] = jobs[0].profit
    for i in range(1,len(jobs)):
        for j in range(i):
            if jobs[j].end_time <= jobs[i].start_time:
                cache[i] = max(cache[i], cache[j]+jobs[i].profit)
    return cache[-1]

if __name__ == '__main__':
    array = [(1,2,50), (3,5,20), (6,19,100), (2,100,200)]
    array = sorted(array, key = lambda x: x[1])
    jobs = []
    for idx,entry in enumerate(array):
        curr_job = Job(idx,entry[0],entry[1],entry[2])
        jobs.append(curr_job)
    print(maxProfit(jobs))
