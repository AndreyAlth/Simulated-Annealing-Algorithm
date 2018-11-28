import random, numpy, math, copy, matplotlib.pyplot as plt
cities = [[239, 235], [-128, 42], [-242, -5], [-93, 77], [-114, -237], [-83, -131], [-270, 171], [-221, 53], [122, 35], [53, -106], [-81, 236], [-105, -296], [-109, -285], [-116, -6], [-52, -184], [144, -102], [-241, 72], [111, -91], [-56, 277], [-206, 200], [-70, -173], [-82, 111], [30, -130], [-230, -265], [153, 299], [24, -61], [244, -36], [-234, -275], [-159, -242], [-298, 213]]
n = len(cities)
tour = random.sample(range(n),n);
for temperature in numpy.logspace(0,5,num=100000)[::-1]:
    [i,j] = sorted(random.sample(range(n),2));
    newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];
    if math.exp( ( sum([ math.sqrt(sum([(cities[tour[(k+1) % n]][d] - cities[tour[k % n]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([ math.sqrt(sum([(cities[newTour[(k+1) % n]][d] - cities[newTour[k % n]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
        tour = copy.copy(newTour);
distanciaT = 0
for i in range(n-1):
    distanciaT += ((cities[tour[i]][0]-cities[tour[i+1]][0])**2+(cities[tour[i]][1]-cities[tour[i+1]][1])**2)**0.5
print(distanciaT)
plt.plot([cities[tour[i % n]][0] for i in range(n+1)], [cities[tour[i % n]][1] for i in range(n+1)], 'xb-');
plt.show()
