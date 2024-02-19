from tabulate import tabulate

# tinggal di run saja
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

# isilah titik - titik di bawah ini
class User:
    
    def __init__(self, username):
        self.username = username
        
    def check_benefit(self):
        # init headers
        headers = ["Basic Plan", "Standard Plan", "Premium Plan"]
        
        # init table
        table = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]
        
        print("===== PacFlix Plan List =====")
        print("")
        print(tabulate(table, headers, tablefmt="grid"))
        
    # create check_plan based on username
    def check_plan(self, username):
        
        # iterate keys and values based on data
        for key, value in data.items():
            
            # create branching
            if key == self.username:
                # create variables to nampung value nya
                get_current_plan = value[0]
                get_duration_plan = value[1]
                
                print(f"Username: {self.username}")
                print(f"Current Plan: {get_current_plan}")
                print(f"Duration Plan: {get_duration_plan} bulan")
                
    # create upgrade_plan method based on username
    def upgrade_plan(self, username, upgrade_plan):
        
        DISCOUNT = 0.05
        
        # iterate keys and values based on data
        for key, value in data.items():
            
            if key == self.username:
                get_current_plan = value[0]
                get_duration_plan = value[1]
                
                if upgrade_plan != get_current_plan:
                    if get_duration_plan > 12:
                        # branching for discount
                        if upgrade_plan == "Basic Plan":
                            total = 120_000 - (120_000 * DISCOUNT)
                            
                            return total
                        
                        elif upgrade_plan == "Standard Plan":
                            total = 160_000 - (160_000 * DISCOUNT)
                            
                            return total
                        
                        elif upgrade_plan == "Premium Plan":
                            total = 200_000 - (200_000 * DISCOUNT)
                            
                            return total
                        
                        else:
                            raise Exception("Plan tidak tersedia")
                            
                    else:
                        # branching not discount
                        if upgrade_plan == "Basic Plan":
                            total = 120_000
                            return total
                        
                        elif upgrade_plan == "Standard Plan":
                            total = 160_000
                            return total
                        
                        elif upgrade_plan == "Premium Plan":
                            total = 200_000
                            return total
                        
                        else:
                            raise Exception("Plan tidak tersedia")
                        
                else:
                    raise Exception("Plan tidak boleh sama!")

# isi titik - titik di bawah ini
class NewUser:
    
    referral_code = []
    
    def __init__(self, username):
        self.username = username
        
    def get_referral_code(self, data):
        
        for value in data.values():
            ref_code = value[2]
            # append to empty list
            self.referral_code.append(ref_code)
            
        return self.referral_code
    
    # create pick_plan method
    def pick_plan(self, new_plan, referral_code):
        
        DISCOUNT = 0.04
        
        if referral_code in self.referral_code:
            if new_plan == "Basic Plan":
                total = 120_000 - (120_000 * DISCOUNT)
                
                return total
            
            elif new_plan == "Standard Plan":
                total = 160_000 - (160_000 * DISCOUNT)
                
                return total
            
            elif new_plan == "Premium Plan":
                total = 200_000 - (200_000 * DISCOUNT)
                
                return total
            
            else:
                raise Exception("Plan tidak tersedia")
            
        
        else:
            raise Exception("Referral Code tidak tersedia")
        
user_1 = User(username = "Shandy")

print(user_1.check_benefit())

print(user_1.upgrade_plan(username = user_1.username,
                          upgrade_plan = "Premium Plan"))