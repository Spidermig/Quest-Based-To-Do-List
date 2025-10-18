python:

    class task:

        name = "this task"

        def __init__(self, name, description, day, time, status):
            self.name = name
            self.description = description
            self.dayOfTheWeek = day #sunday, monday, tuesday, wednesday, thursday, friday, saturday
            self.timeOfDay = time #morning, afternoon, evening
            self.status = status
        
        def updateStatus(nStatus):
            self.status = nStatus

    
        