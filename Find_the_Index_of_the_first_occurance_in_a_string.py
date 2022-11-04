s="kin"
t="uhiuhvpuizhyickinhuckkinwu"

if len(s) > len(t):
    print(-1)
l, r  = 0, len(s)
while l < len(t):
    if t[l:r] != s:
        l += 1
        r += 1
    elif t[l:r] == s:
        print(l+1)
        break