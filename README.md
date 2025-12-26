<h2 data-start="364" data-end="378">What is it?</h2>
<p data-start="380" data-end="459"><strong data-start="380" data-end="400">TCP Port Monitor</strong> is a Home Assistant custom integration that allows you to:</p>
<ul data-start="461" data-end="766">
<li data-start="461" data-end="526">
<p data-start="463" data-end="526">Check the availability of any TCP port on a server or service</p>
</li>
<li data-start="527" data-end="577">
<p data-start="529" data-end="577">Measure connection <strong data-start="548" data-end="559">latency</strong> in milliseconds</p>
</li>
<li data-start="578" data-end="639">
<p data-start="580" data-end="639">Customize <strong data-start="590" data-end="607">scan interval</strong>, <strong data-start="609" data-end="620">timeout</strong>, and <strong data-start="626" data-end="637">retries</strong></p>
</li>
<li data-start="640" data-end="694">
<p data-start="642" data-end="694">Manage sensors directly from the Home Assistant UI</p>
</li>
<li data-start="695" data-end="766">
<p data-start="697" data-end="766">Remove the integration completely without leaving orphaned entities</p>
</li>
</ul>
<p data-start="768" data-end="815">It creates <strong data-start="779" data-end="814">two entities per monitored port</strong>:</p>
<ol data-start="817" data-end="949">
<li data-start="817" data-end="888">
<p data-start="820" data-end="888"><strong data-start="820" data-end="837">Binary Sensor</strong> &mdash; shows whether the port is reachable (<code data-start="877" data-end="885">on/off</code>)</p>
</li>
<li data-start="889" data-end="949">
<p data-start="892" data-end="949"><strong data-start="892" data-end="910">Latency Sensor</strong> &mdash; shows the connection latency in ms</p>
</li>
</ol>
<hr data-start="951" data-end="954" />
<h2 data-start="956" data-end="980">Installation via HACS</h2>
<h3 data-start="982" data-end="1013">Step 1 &mdash; Add the repository</h3>
<ol data-start="1015" data-end="1122">
<li data-start="1015" data-end="1072">
<p data-start="1018" data-end="1072">Open <strong data-start="1023" data-end="1070">Home Assistant &rarr; HACS &rarr; Custom repositories</strong></p>
</li>
<li data-start="1073" data-end="1091">
<p data-start="1076" data-end="1091">Click <strong data-start="1082" data-end="1089">Add</strong></p>
</li>
<li data-start="1092" data-end="1122">
<p data-start="1095" data-end="1122">Paste the repository URL:</p>
</li>
</ol>
<div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary">
<div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9">&nbsp;</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!">https://github.com/YourGitHubUsername/port_monitor </code></div>
</div>
<ol start="4" data-start="1184" data-end="1246">
<li data-start="1184" data-end="1227">
<p data-start="1187" data-end="1227">Select <strong data-start="1194" data-end="1209">Integration</strong> as the category</p>
</li>
<li data-start="1228" data-end="1246">
<p data-start="1231" data-end="1246">Click <strong data-start="1237" data-end="1244">ADD</strong></p>
</li>
</ol>
<hr data-start="1248" data-end="1251" />
<h3 data-start="1253" data-end="1289">Step 2 &mdash; Install the integration</h3>
<ol data-start="1291" data-end="1418">
<li data-start="1291" data-end="1325">
<p data-start="1294" data-end="1325">Go to <strong data-start="1300" data-end="1323">HACS &rarr; Integrations</strong></p>
</li>
<li data-start="1326" data-end="1356">
<p data-start="1329" data-end="1356">Find <strong data-start="1334" data-end="1354">TCP Port Monitor</strong></p>
</li>
<li data-start="1357" data-end="1390">
<p data-start="1360" data-end="1390">Click <strong data-start="1366" data-end="1388">Download / Install</strong></p>
</li>
<li data-start="1391" data-end="1418">
<p data-start="1394" data-end="1418">Restart Home Assistant</p>
</li>
</ol>
<hr data-start="1420" data-end="1423" />
<h3 data-start="1425" data-end="1475">Step 3 &mdash; Add the integration in Home Assistant</h3>
<ol data-start="1477" data-end="1851">
<li data-start="1477" data-end="1539">
<p data-start="1480" data-end="1539">Go to <strong data-start="1486" data-end="1537">Settings &rarr; Devices &amp; Services &rarr; Add Integration</strong></p>
</li>
<li data-start="1540" data-end="1576">
<p data-start="1543" data-end="1576">Search for <strong data-start="1554" data-end="1574">TCP Port Monitor</strong></p>
</li>
<li data-start="1577" data-end="1829">
<p data-start="1580" data-end="1616">Enter the following configuration:</p>
<ul data-start="1620" data-end="1829">
<li data-start="1620" data-end="1661">
<p data-start="1622" data-end="1661"><strong data-start="1622" data-end="1630">Host</strong> &mdash; IP or domain of the server</p>
</li>
<li data-start="1665" data-end="1697">
<p data-start="1667" data-end="1697"><strong data-start="1667" data-end="1675">Port</strong> &mdash; TCP port to check</p>
</li>
<li data-start="1701" data-end="1746">
<p data-start="1703" data-end="1746"><strong data-start="1703" data-end="1720">Scan interval</strong> &mdash; optional, default 30s</p>
</li>
<li data-start="1750" data-end="1788">
<p data-start="1752" data-end="1788"><strong data-start="1752" data-end="1763">Timeout</strong> &mdash; optional, default 2s</p>
</li>
<li data-start="1792" data-end="1829">
<p data-start="1794" data-end="1829"><strong data-start="1794" data-end="1805">Retries</strong> &mdash; optional, default 2</p>
</li>
</ul>
</li>
<li data-start="1830" data-end="1851">
<p data-start="1833" data-end="1851">Click <strong data-start="1839" data-end="1849">Submit</strong></p>
</li>
</ol>
<hr data-start="1853" data-end="1856" />
<h3 data-start="1858" data-end="1876">Step 4 &mdash; Usage</h3>
<p data-start="1878" data-end="1916">After adding, two sensors will appear:</p>
<ul data-start="1918" data-end="2045">
<li data-start="1918" data-end="1972">
<p data-start="1920" data-end="1972"><code data-start="1920" data-end="1944">binary_sensor.port_xxx</code> &mdash; shows port availability</p>
</li>
<li data-start="1973" data-end="2045">
<p data-start="1975" data-end="2045"><code data-start="1975" data-end="2000">sensor.port_xxx_latency</code> &mdash; shows connection latency in milliseconds</p>
</li>
</ul>
<p data-start="2047" data-end="2066">Example automation:</p>
<div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary">
<div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9">&nbsp;</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-yaml"><span class="hljs-attr">automation:</span> <span class="hljs-bullet">-</span> <span class="hljs-attr">alias:</span> <span class="hljs-string">Notify</span> <span class="hljs-string">if</span> <span class="hljs-string">service</span> <span class="hljs-string">port</span> <span class="hljs-string">is</span> <span class="hljs-string">down</span> <span class="hljs-attr">trigger:</span> <span class="hljs-attr">platform:</span> <span class="hljs-string">state</span> <span class="hljs-attr">entity_id:</span> <span class="hljs-string">binary_sensor.port_1_2_3_4_443</span> <span class="hljs-attr">to:</span> <span class="hljs-string">"off"</span> <span class="hljs-attr">action:</span> <span class="hljs-attr">service:</span> <span class="hljs-string">notify.mobile_app</span> <span class="hljs-attr">data:</span> <span class="hljs-attr">message:</span> <span class="hljs-string">"Service port is unreachable!"</span> </code></div>
</div>
<hr data-start="2339" data-end="2342" />
<h3 data-start="2344" data-end="2361">Step 5 &mdash; Tips</h3>
<ul data-start="2363" data-end="2582">
<li data-start="2363" data-end="2448">
<p data-start="2365" data-end="2448">Make sure the server or service you monitor has the TCP port open and accessible.</p>
</li>
<li data-start="2449" data-end="2512">
<p data-start="2451" data-end="2512">The latency sensor updates only when the port is reachable.</p>
</li>
<li data-start="2513" data-end="2582">
<p data-start="2515" data-end="2582">Removing the integration will fully clean up all related sensors.</p>
</li>
</ul>
