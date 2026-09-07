class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)

        time = [((target-p)/s) for p,s in pair]

        car_fleets = 1
        last_fastest_time = time[0]
        for i in range(1,len(time)):
            if time[i] > last_fastest_time:
                car_fleets += 1
                last_fastest_time = time[i]

        return car_fleets