# QueueLess AI Architecture
User/staff → current queue data → feature preparation → Random Forest regression → predicted waiting time → compare counters → fastest-queue recommendation.

Six model inputs: queue length, average service time, hour, day of week, arrival rate and counter efficiency.
