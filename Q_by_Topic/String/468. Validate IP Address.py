class Solution:
    def check_IPv4(self, IP):
        if(len(IP) != 4):
            return "Neither"
        for w in IP:
            if(len(w) == 0):
                return "Neither"
            elif(w[0] == "0" and w != "0"):
                return "Neither"
            else:
                try:
                    num = int(w)
                    if(not 0 <= num <= 255):
                        return "Neither"
                except:
                    return "Neither"
        return "IPv4"

                        
    def check_IPv6(self,IP):
        if(len(IP) != 8):
            return "Neither"
        for w in IP:
            if(len(w) > 4):
                return "Neither"
            try:
                num = int(w, base = 16)
            except:
                return "Neither"
        return "IPv6"

    
    def validIPAddress(self, IP):
        if("." in IP and ":" in IP):
            return "Neither"
        elif("." in IP):
            IP = IP.split(".")
            return self.check_IPv4(IP)
        elif(":" in IP):
            IP = IP.split(":")
            return self.check_IPv6(IP)
        else:
            return "Neither"


IP = "172.16.254.1"
sol = Solution()
print(sol.validIPAddress(IP))
