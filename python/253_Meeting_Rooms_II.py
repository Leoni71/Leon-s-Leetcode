# Method 1: Priority Queues(Heap)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free_rooms = []
        intervals.sort(key=lambda x:x[0])
        
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)
      
# Method 2: Chronological Ordering(Two pointers)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])
        l = len(intervals)
        
        s_ptr, e_ptr = 0, 0
        while s_ptr < l:
            if start_timings[s_ptr] >= end_timings[e_ptr]:
                e_ptr += 1
            s_ptr += 1
    
        return s_ptr-e_ptr
