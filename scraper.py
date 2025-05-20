text
  python-2.7.14
import scraperwiki
html = scraperwiki.scrape('https://web.archive.org/web/20120318184750/http://www.inmo.ie/6022')
print "Click on the ...more link to see the whole page"
print html
import lxml.html
root = lxml.html.fromstring(html)
tds = root.cssselect('td')
for td in tds:
  print lxml.html.tostring(td)
  print td.text
for td in tds:
  record = { "td" : td.text }
  scraperwiki.sqlite.save(["td"], record)
