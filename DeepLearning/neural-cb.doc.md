Test thử trên tập 10K ratings

Evaluation Metrics:
RMSE: 0.7480823993682861
MAE: 0.4860612750053406

Top 10

{'A3PB71Q63XF43G': array(['B00021DUM2', 'B00021DUMW', 'B0001BOD1U', 'B0002GPZSO',
'B000N30WYI', 'B000GEF8NO', 'B000K1YMJO', 'B000MRTXR2',
'B0001K55NG', 'B0001EKYG0'], dtype='<U10')}
20982 Bare Escentuals bareMinerals Blush
Name: Title, dtype: object
20981 SUI DREAMS For Women By ANNA SUI Eau De Toilet...
Name: Title, dtype: object
29302 Creed Spring Flower by Creed for Women - 2.5 o...
Name: Title, dtype: object
21426 Day Off by Day Off for Women Eau De Toilette S...
Name: Title, dtype: object
13336 Blue Orchidee Solid Perfume 5 g by Crazylibell...
Name: Title, dtype: object
11958 Blooming Body Belly Bliss - Ultimate Anti-Itch...
Name: Title, dtype: object
18935 L'epi de Provence Triple Milled Shea Butter Ve...
Name: Title, dtype: object
28364 Neova Toning Creme 2 oz.
Name: Title, dtype: object
19386 Kayline Dryer & 3-irons Pedestal Appliance Hol...
Name: Title, dtype: object
3060 Exuviance Moisture Balance Toner
Name: Title, dtype: object

Total time for recommending top N: 0.019248485565185547 seconds
Memory usage: 553.63671875 MB

### Save model

# Lưu mô hình đã huấn luyện

model_path = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/DeepLearning/model/neural_collaborative'

ncf.save(path=model_path, model_name='ncf_model')
print("Model saved successfully!")

Nhận thấy là với tập 10k rating nhưng quá trình train chỉ tốn 553MB ram => thử tiếp tục với tập dataset lớn hơn so với các thuật toán khác:

### Tập 30k

Evaluation Metrics:
RMSE: 0.9168535470962524
MAE: 0.45019686222076416

Recommendations:
{'A3PB71Q63XF43G': array(['B000FTYRJG', 'B000IL7E5K', 'B000MOWGME', 'B000H0SCXU',
'B00006FE2Z', 'B000C1VTNO', 'B000JK6WYE', 'B000JPI91S',
'B000E7SSDK', 'B0009N35VO'], dtype='<U10')}
26576 Blue Spring Salon Peach Stuff Facial Moisturiz...
Name: Title, dtype: object
21490 JAQUA Pink Champagne Sinfully Rich Shea Body B...
Name: Title, dtype: object
7703 CALIFORNIA TAN TOTAL SUBMERSION STEP 3 TAN EXT...
Name: Title, dtype: object
14312 Pureology Hydrate Condition
Name: Title, dtype: object
3674 Neutrogena Oil-Free Deep Clean Gentle Scrub, 4...
3675 Neutrogena Oil-Free Deep Clean Gentle Scrub, 4...
Name: Title, dtype: object
6066 Candies By Liz Claiborne For Men. Cologne Spra...
Name: Title, dtype: object
22464 Jennifer Lopez Glow Eau de Toilette Spray
Name: Title, dtype: object
21595 Redken Satinwear 02 Ultimate Blow-dry Lotion 5oz
21596 Redken Satinwear 02 Ultimate Blow-dry Lotion 5oz
Name: Title, dtype: object
22364 Jaguar Cologne by Jaguar for men Colognes
22365 Jaguar Cologne by Jaguar for men Colognes
Name: Title, dtype: object
28367 Samsara
Name: Title, dtype: object

Total time for recommending top N: 0.028936386108398438 seconds
Memory usage: 600.390625 MB

### Tiếp tục test trên tập 100k ratings

Evaluation Metrics:
RMSE: 0.9168535470962524
MAE: 0.45019686222076416

Name: Title, dtype: object
Recommendations:
{'A3PB71Q63XF43G': array(['B000FTYRJG', 'B000IL7E5K', 'B000MOWGME', 'B000H0SCXU',
'B00006FE2Z', 'B000C1VTNO', 'B000JK6WYE', 'B000JPI91S',
'B000E7SSDK', 'B0009N35VO'], dtype='<U10')}
26576 Blue Spring Salon Peach Stuff Facial Moisturiz...
Name: Title, dtype: object
21490 JAQUA Pink Champagne Sinfully Rich Shea Body B...
Name: Title, dtype: object
7703 CALIFORNIA TAN TOTAL SUBMERSION STEP 3 TAN EXT...
Name: Title, dtype: object
14312 Pureology Hydrate Condition
Name: Title, dtype: object
3674 Neutrogena Oil-Free Deep Clean Gentle Scrub, 4...
3675 Neutrogena Oil-Free Deep Clean Gentle Scrub, 4...
Name: Title, dtype: object
6066 Candies By Liz Claiborne For Men. Cologne Spra...
Name: Title, dtype: object
22464 Jennifer Lopez Glow Eau de Toilette Spray
Name: Title, dtype: object
21595 Redken Satinwear 02 Ultimate Blow-dry Lotion 5oz
21596 Redken Satinwear 02 Ultimate Blow-dry Lotion 5oz
Name: Title, dtype: object
22364 Jaguar Cologne by Jaguar for men Colognes
22365 Jaguar Cologne by Jaguar for men Colognes
Name: Title, dtype: object
28367 Samsara
Name: Title, dtype: object
Total time for recommending top N: 0.027625083923339844 seconds

Memory usage: 594.69140625 MB

### Train trên full tập 200k rating

Evaluation Metrics:
RMSE: 0.9168535470962524
MAE: 0.45019686222076416

Recommendations:
{'A3PB71Q63XF43G': array(['B000FTYRJG', 'B000IL7E5K', 'B000MOWGME', 'B000H0SCXU',
'B00006FE2Z', 'B000C1VTNO', 'B000JK6WYE', 'B000JPI91S',
'B000E7SSDK', 'B0009N35VO'], dtype='<U10')}
26576 Blue Spring Salon Peach Stuff Facial Moisturiz...
Name: Title, dtype: object
21490 JAQUA Pink Champagne Sinfully Rich Shea Body B...
Name: Title, dtype: object
7703 CALIFORNIA TAN TOTAL SUBMERSION STEP 3 TAN EXT...
Name: Title, dtype: object
14312 Pureology Hydrate Condition
Name: Title, dtype: object
3674 Neutrogena Oil-Free Deep Clean Gentle Scrub, 4...
3675 Neutrogena Oil-Free Deep Clean Gentle Scrub, 4...
Name: Title, dtype: object
6066 Candies By Liz Claiborne For Men. Cologne Spra...
Name: Title, dtype: object
22464 Jennifer Lopez Glow Eau de Toilette Spray
Name: Title, dtype: object
21595 Redken Satinwear 02 Ultimate Blow-dry Lotion 5oz
21596 Redken Satinwear 02 Ultimate Blow-dry Lotion 5oz
Name: Title, dtype: object
22364 Jaguar Cologne by Jaguar for men Colognes
22365 Jaguar Cologne by Jaguar for men Colognes
Name: Title, dtype: object
28367 Samsara
Name: Title, dtype: object

Total time for recommending top N: 0.02485823631286621 seconds
Memory usage: 596.21875 MB

Vẫn không tiêu tốn quá nhiều CPU và RAM

Thấy vẫn còn nhẹ nhàng nên thử tăng số epoc lên 100:

ncf = NCF(
task="rating",
data_info=data_info,
n_epochs=100,
)

Kết quả:
Evaluation Metrics:
RMSE: 0.9283047318458557
MAE: 0.48171862959861755

Recommendations:
{'A3PB71Q63XF43G': array(['B000C1ZCP0', 'B000NNLJW2', 'B000KOM91Y', 'B0006NZKAG',
'B000FGXARO', 'B000P276BE', 'B000NCTTGQ', 'B000K73CNK',
'B0001TMDF0', 'B0006GR8M6'], dtype='<U10')}
6802 Ciara 200% by Revlon for Women, Cologne Spray,...
Name: Title, dtype: object
20989 HEAVEN SENT by Dana
Name: Title, dtype: object
14835 Natural Match 6W Light Golden Brown Women's Ha...
Name: Title, dtype: object
19987 YARDLEY by Yardley for WOMEN: LILY OF THE VALL...
Name: Title, dtype: object
5661 Shiseido The Makeup Mascara Base --7 ml
Name: Title, dtype: object
31077 Jessica Mc Clintock Silk Ribbon by Jessica Mcc...
Name: Title, dtype: object
19178 CUCCIO NATURALE Lavender Environmental Hand Pr...
Name: Title, dtype: object
26554 SEPHORA COLLECTION Vanity Brush Set (20 Value)...
Name: Title, dtype: object
19822 Heritage Products Rosewater
19823 Heritage Products Rosewater
Name: Title, dtype: object
30125 Paul Mitchell Tea Tree Special Shampoo 32 OZ
Name: Title, dtype: object
Total time for recommending top N: 0.0260622501373291 seconds
Memory usage: 582.31640625 MB

![alt text](../Pictures/Screenshot_20250101_141024.png)
