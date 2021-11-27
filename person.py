
class Person:

    def __init__(self, legal_name = "Hao Yu", perfer_name = "Caffrey Yu"):
        self.name = legal_name
        self.pname = perfer_name
    
    def setMaster(self, degree, school, dept, program):
        self.msd = degree
        self.mss = school
        self.msd = dept
        self.msp = program
    
    def setBachelor(self, degree, school, majors, year, month, minors = None, honor = ""):
        self.bsd = degree
        self.bss = school
        self.bsmajors = majors
        self.bsminors = minors
        self.bsy = year
        self.bsm = month
        self.bsh = honor
    
    def __call__(self):
        intro = "+ My name is %s. That's my legal name. My preferred name is %s. "
        ms = "+ Currently I am a first year M.S. student in the %s department at %s studying %s. "
        bs = "+ I graduated %s from %s in %s %s with %s in %s%s. "
        bg = "+ I am a robotics engineer with 4+ years of experience working with various platforms. "
        bg2 = "+ I have abundant experience in robotics software and the perception field. "
        intro_data = (self.name, self.pname)
        ms_data = (self.mss, self.msd, self.msp)
        bs_data = [self.bsh, self.bss, self.bsm, self.bsy]
        
        if len(self.bsmajors) > 1: 
            bs_data.append("majors")
            majors = ["%s"] * len(self.bsmajors)
            temp = "and".format(majors)
            temp = temp % self.bsmajors
            bs_data.append(temp)

        elif len(self.bsmajors) == 1: 
            bs_data.append("a major")
            bs_data.append(self.bsmajors[0])
        
        if self.bsminors:
            temp = []
            if len(self.bsminors) > 1:
                temp.append(" and minors in")
                temp.append(" and ".join(self.bsminors))
            else: 
                temp.append(" and a minor in")
                temp.append(self.bsminors[0])
            bs_data.append(" ".join(temp))
        else:
            bs_data.append("")

        bs_data = tuple(bs_data)

        res = "%s \n%s \n%s" 
        res_data = (intro % intro_data, ms % ms_data, bs % bs_data)

        print (res % res_data)


