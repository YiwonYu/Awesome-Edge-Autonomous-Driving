"""Bounded reachability check; HTTP success does not establish source validity."""
import concurrent.futures,datetime,json,pathlib,re,subprocess
root=pathlib.Path(__file__).resolve().parents[1]
urls=set()
for path in root.glob('*.md'):
 urls.update(re.findall(r'https?://[^\s<>\)]+',path.read_text()))
for r in json.loads((root/'catalog.json').read_text()):
 for key in ('paper','code'):
  if r[key].startswith('http'):urls.add(r[key])
def check(url):
 try:
  r=subprocess.run(['curl','-L','--max-time','18','--connect-timeout','7','-s','-o','/dev/null','-w','%{http_code}\t%{url_effective}',url],capture_output=True,text=True,timeout=20)
  status,_,final=r.stdout.partition('\t')
  return dict(url=url,http_status=status,final_url=final,result='reachable' if status=='200' else 'inconclusive' if status in ('000','403','429') or r.returncode else 'review',curl_exit=r.returncode)
 except Exception as e:return dict(url=url,result='inconclusive',error=type(e).__name__)
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool: results=list(pool.map(check,sorted(urls)))
(root/'link-checks.json').write_text(json.dumps(dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),method='HTTP GET with redirects; bounded timeout; no content-equivalence guarantee',results=results),indent=2)+'\n')
print('Checked',len(results),'URLs')
for r in results:
 if r['result']!='reachable':print(r)
