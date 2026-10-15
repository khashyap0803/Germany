import json
p=open('plan.json',encoding='utf8').read(); json.loads(p)
p=p.replace('</','<\/')
t=open('template.html',encoding='utf8').read()
open('germany-2028-planner.html','w',encoding='utf8').write(t.replace('__PLAN__',p))
open('preview.html','w',encoding='utf8').write('<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'+t.replace('__PLAN__',p))
