from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("wordcloud_3.csv",encoding="utf-8")  #워드클라우드로 만들기 위한 데이터
wc = df.set_index("title").to_dict()["count"]

wordCloud = WordCloud(
    font_path='/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf',  #google colabs 에서 하기 위함
    width = 400,
    height = 400,
    colormap = 'viridis',
    max_font_size=80,
    background_color='white'
).generate_from_frequencies(wc)

plt.figure()
plt.imshow(wordCloud)
plt.axis('off')