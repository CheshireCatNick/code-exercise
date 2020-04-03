class UndergroundSystem:

    def __init__(self):
        # id to last check in place and time
        self.start = {}
        # avg[start][end] = []
        # index 0 is sum
        # index 1 is record count
        self.avg = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        [start, startTime] = self.start[id]
        duration = t - startTime
        end = stationName
        if start in self.avg:
            if end in self.avg[start]:
                self.avg[start][end][0] += duration
                self.avg[start][end][1] += 1
            else:
                self.avg[start][end] = [duration, 1]
        else:
            self.avg[start] = {}
            self.avg[start][end] = [duration, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        result = self.avg[startStation][endStation]
        return result[0] / result[1]
        

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))
# 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
#11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
#11.0
undergroundSystem.checkOut(10, "Waterloo", 38)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
#12.0