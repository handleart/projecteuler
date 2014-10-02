#Project Euler, Problem 15
#How many (such) routes are there through a 20x20 grid?
# general solution for lattice problems is (m n)

n = 20
m = 20

# (n+m)! / (m! * n!)

mn = m + n
mn_fac = 1
n_fac = 1
m_fac = 1


for i in range(1, mn+1):
	mn_fac = mn_fac * i

for i in range(1, m+1):
	m_fac = m_fac * i


for i in range(1, n+1):
	n_fac = n_fac * i


print (mn_fac / (n_fac * m_fac))