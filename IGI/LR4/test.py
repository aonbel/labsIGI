import re
import numpy as np

print(re.findall("\w\w", "AV did idic didn"))

class A:

    def get_sex(self):
        return self._sex
    
    def set_sex(self, value):
        print("sex was set")
        self._sex = value

    def del_sex(self):
        print("sex was deleted")

    sex = property(get_sex, set_sex, del_sex, "sex")

a = A()
a.sex = "sex"

result = re.findall(r'\@(\w+)\.(\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)


r = re.compile("\w+")

print(re.findall(r, "asdasd asdasdasdas asdasd"))
print(r.findall("asdasd adsasdasdasd adsasd"))
np.random.random((3,4))

