# Autorec

## Tập 100 record

Tham số: epochs=100, hiddenDim=100, learningRate=0.01, batchSize=100, sim_options={}

Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
AutoRec 2.0318 1.5776 0.0000 0.0000 0.0000 0.9878 0.9340 12.3410

Top 10:

We recommend:
Island Essence Lotion: 4.21
Glysomed Body Lotion, 8.5-Ounce Bottles: 4.21
Curve Crush FOR WOMEN by Liz Claiborne - 0.50 oz EDT Spray: 4.21
Oscar Eau de Toilette for Women by Oscar de La Renta: 1.00
Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 1.00
Michel Design Works Bath Gift Set - Beach: 1.00
Liz Claiborne Curve Eau de Toilette Spray: 1.00
Palladio Herbal Lipstick,: 1.00
SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 1.00
Island Essence Lotion: 1.00

Total time for recommending top N: 0.37696170806884766 seconds
Memory usage: 291.765625 MB

Thử chạy để dò tham số tối ưu:
param_grid = {'hiddenDim': [120, 50, 200], 'learningRate': [0.00001, 0.05, 0.1]}

Best RMSE score attained: 1.3744000277682027
{'hiddenDim': 200, 'learningRate': 0.05}

Kết quả

Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
AutoRecTuned 1.8469 1.4704 0.0000 0.0000 0.0000 1.0000 0.9789 10.0024

We recommend:
Oscar Eau de Toilette for Women by Oscar de La Renta: 4.21
Michel Design Works Bath Gift Set - Beach: 4.21
Liz Claiborne Curve Eau de Toilette Spray: 4.21
Palladio Herbal Lipstick,: 4.21
SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.21
Island Essence Lotion: 4.21
Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.21
Island Essence Lotion: 4.21
Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.21
Old Spice High Endurance Hair & Body Wash 23.6 Fl oz: 4.21
Total time for recommending top N: 0.40456175804138184 seconds
Memory usage: 289.34765625 MB

Có thể thấy các chỉ số HR, cHR và ARHR thấp tới mức không có điểm => điều đó chứng tỏ đối với data mà model chưa gặp bao giờ thì sẽ không đoán được

## Tập 10k record

### Untuned

Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
AutoRec 1.4390 1.1140 0.0006 0.0006 0.0003 1.0000 0.9758 553.2887

We recommend:
Oscar Eau de Toilette for Women by Oscar de La Renta: 4.17
Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 4.17
Michel Design Works Bath Gift Set - Beach: 4.17
Liz Claiborne Curve Eau de Toilette Spray: 4.17
Palladio Herbal Lipstick,: 4.17
SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.17
Island Essence Lotion: 4.17
Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.17
Island Essence Lotion: 4.17
Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.17
Total time for recommending top N: 803.0699920654297 seconds
Memory usage: 1372.1640625 MB
