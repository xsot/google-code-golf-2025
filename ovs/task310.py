p=lambda a,*n:[b for b in zip(*n or p(a,*a))if{*b}-({*a[1]}&{*a[12]})]
