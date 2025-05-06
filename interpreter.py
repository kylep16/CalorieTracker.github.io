from textx import metamodel_from_file
tracker_mm = metamodel_from_file('calorietracker.tx')
tracker_model = tracker_mm.model_from_file('day1.ct')

class Tracker:
    
    def __init__(self):
        self.healthycalories = 0
        self.junkcalories = 0
        self.neutralcalories = 0
        self.totalcalories = 0
        self.height = 0
        self.weight = 0
        self.goal = 0
        self.bmi = 0

    def interpret(self, model):
        print("CALORIE TRACKER STAT KEEPER")
        print("STAY HEALTHY AND PANDA STAYS HEALTHY\n")
    
    # model is an instance of Program
        
        for c in model.commands:
            if c.__class__.__name__ == "GoalCommand":
                print(f"Your goal {c.goal} is calories\n")
                self.goal = c.goal
            
            if c.__class__.__name__ == "ModeCommand":
                print(f"MODE SET TO {c.mode} MODE, ADJUSTING PLAN\n")
                
                if c.mode == "bulk":
                    self.goal += 500
                    print("YOUR NEW GOAL IS", self.goal , "NOW\n")
                
                elif c.mode == "cut":
                    self.goal -= 1000
                    print("YOUR NEW GOAL IS", self.goal , "NOW\n")
            
            if c.__class__.__name__ == "HeightCommand":
                print(f"You are {c.height} inches tall")
                self.height = c.height
            
            if c.__class__.__name__ == "WeightCommand":
                print(f"You weigh {c.weight} pounds\n")
                self.weight = c.weight
            
            if c.__class__.__name__ == "HealthyFoodCommand":
                self.healthycalories += c.calories
                self.totalcalories += c.calories

            if c.__class__.__name__ == "JunkFoodCommand":
                self.junkcalories += c.calories
                self.totalcalories += c.calories


                
        self.bmi = round((self.weight / (self.height * self.height)) * 703,2)
        
        
        print("Your BMI is ", self.bmi, "\n")
        
        
        if self.bmi < 18.5:
            print("You Have Underweight BMI\n")
        elif self.bmi > 18.5 and self.bmi < 24.9:
            print("You Have Average BMI\n")
        else: 
            print("You Have Overweight Bmi")

        
        print(f"You had {self.healthycalories} healthy calories today\n")
        print(f"You had {self.junkcalories} junk calories today\n")
        
        if self.goal > self.totalcalories:
            print("Calorie Goal Not Achieved\n")
            Under = self.goal - self.totalcalories
            print("You were under by", Under, "\n")
            achieve = False
            
        elif self.goal < self.totalcalories:
            print("Calorie Goal Not Achieved\n")
            Over = self.totalcalories - self.goal
            print("You were over by", Over, "\n")
            achieve = False


        else:
            print("You Hit Your Goal!!!!\n")
            achieve = True

        if self.junkcalories > self.healthycalories:
            print("Panda is sick because you ate more junk food than healthy food\n")
            print("(｡•́︿•̀｡)\n")  
        
        if self.junkcalories < self.healthycalories:
            print("Panda is happy you ate less junk food today")
            print("ฅ՞•ﻌ•՞ฅ\n")
        
tracker = Tracker()
tracker.interpret(tracker_model)
