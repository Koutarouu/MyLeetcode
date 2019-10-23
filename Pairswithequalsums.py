a=list(map(int, input().split()))
"""h={}
for i in range(len(a)):
	for j in range(i+1, len(a)):
		sma=a[i] + a[j]
		if sma in h and len(h[sma])<2:
			h[sma].append((a[i], a[j]))
			print(h[sma])
			#continue
		h[sma] = [(a[i],a[j])]
#print(h)
"""
h={}
l,r=0,len(a)-1

while l<=(r//2)+1:
	suma=a[l]+a[r]
	cl,cr=l+1,r-1;
	h[suma]=[(a[l],a[r])]
	while cl+1 <= cr-1:
		if suma in h:
			h[suma].append((a[cl], a[cr]))
			cl+=1
			cr-=1
			continue
		h[suma]=[(a[cl],a[cr])]
		cl+=1
		cr-=1
	l+=1
	r-=1
print(h)
