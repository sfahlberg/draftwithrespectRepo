# make_thoughts_page.py
# Patrick Ye

F = open("index.html", "r")
G = F.read()

idx_start = G.index('</nav>')

thoughts = """
 
<div id=\'jumbotron6\' class=\'jumbotron text-center\'>
	<h2>Thoughts about using this site</h2>
	<p>It seems simple at first: find all the NFL players who have done bad things and put them on a website for fantasy league managers to look up. People become more aware of domestic violence, and feel good about not drafting the wrong NFL players. But while domestic violence is obviously bad, the path to judgement is not straightforward.</p>
	<p>The criminal justice system is not optimal. Only a small fraction of accusations result in convictions as overwhelming evidence is required by the legal system. Settlements are common; while presumably satisfying both parties, there is no clear outcome for public records.</p>
	<p>Our culture, while improving in recent years, poses another obstacle for victims stepping forward. These women may feel intimidated to speak up, either because of the abusers themselves who have significantly more wealth and fame, or because of sports fans and their reverence for high-achieving professional athletes. This can understandably lead to indecision, but delays in reporting incidents can cast additional doubt of the victim\'s account.</p>
	<p>Beyond the justice system, how do you decide if a player is not deserving of your fantasy team? Has the player admitted guilt and is truly apologetic? Has the player taken any steps to become a better person?</p>
	<p>We leave it up to you, the fan, to decide for yourself. We at #draftwithrespect can do our job of presenting the data to the best of our ability. Our goal is to help you make your dream fantasy team, both on the field and off the field.</p>
</div> 
"""
      

H = G[0:idx_start+6] + thoughts + G[idx_start+7:]

J = open("thoughts.html", "w")
J.write(H)