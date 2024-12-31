Source for Deep Learning method

Dữ liệu 100 ratings:

Untuned:

Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
RBM - Untuned 1.6080 1.3626 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000

We recommend:
Computing recommendations...
Liz Claiborne Curve Eau de Toilette Spray: 3.03
Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 2.98
Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 2.92
Island Essence Lotion: 2.90
MD Skincare Alpha-Beta Daily Face Peel: 2.90
MAC Eye Shadow -- Parfait Amour (Boxed) 1.5g/0.05oz: 2.89
Old Spice High Endurance Hair & Body Wash 23.6 Fl oz: 2.88
Island Essence Lotion: 2.83
Palladio Liquid Eyeliner #262 Lavender: 2.82
Island Essence Lotion: 2.82
Total time for recommending top N: 0.016982316970825195 seconds
Memory usage: 291.2109375 MB

Tăng data lên 10k:

Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
RBM - Untuned 1.3760 1.1125 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000

Top 10:
We recommend:
Computing recommendations...
NEW cnd Nail Design Stickey Base Coat 0.33Oz: 3.13
BVLGARI for Men By BVLGARI Eau De Toilette Spray: 3.12
Polo Sport by Ralph Lauren for Women, Eau De Toilette Natural Spray: 3.11
Hugo Boss Energise For Men EDT Perfume: 3.10
France Luxe Rectangle Volume Barrette - Classic: 3.10
Revlon Frost & Glow Highlighting Kit 1 ea: 3.10
France Luxe Rectangle Volume Barrette - Classic: 3.10
Buf-Puf Buf-Puf Gentle Facial Sponge: 3.10
France Luxe Rectangle Volume Barrette - Classic: 3.10
Alba Botanica Hawaiian Hand & Body Lotion: 3.10
Total time for recommending top N: 0.11211657524108887 seconds
Memory usage: 2466.33984375 MB

## Tuned

100 record:

Kết quả chạy tìm tham số phù hợp:
Best RMSE score attained: 1.4376548120176775
{'hiddenDim': 20, 'learningRate': 0.1}

Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
RBM - Tuned 1.5612 1.3166 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000

Top 10:
We recommend:
Computing recommendations...
Exuviance Purifying Cleansing Gel-7.2 oz: 3.20
Neutrogena Energizing Sugar Body Scrub, Fresh Citrus, 6 Ounce (Pack of 2): 3.11
Alter Ego, Scented for Women: 3.08
Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 3.08
Focus 21 Jojoba Shampoo 32oz.: 3.08
Exuviance Moisture Balance Toner: 3.08
Pevonia Evolutive Eye Gel "C" (1.0 oz): 3.08
Island Essence Lotion: 3.08
Island Essence Lotion: 3.08
Island Essence Lotion: 3.08
Total time for recommending top N: 0.019118070602416992 seconds
Memory usage: 288.27734375 MB

Thấy kết quả chưa như mong đợi, thử thực hiện dò trên các tổ hợp sau để tìm ra các tham số hợp lý:

```
param_grid = {'hiddenDim': [200, 100, 50, 150, 70], 'learningRate': [0.5, 0.01, 0.001, 0.002, 0.0001]}
gs = GridSearchCV(RBMAlgorithm, param_grid, measures=['rmse', 'mae'], cv=3)
```

Kết quả đạt được:
Best RMSE score attained: 1.4033404157522593
{'hiddenDim': 150, 'learningRate': 0.0001}

Tuy nhiên khi evaluate lại lần nữa với cùng tham số, kết quả đạt được chỉ là:
Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
RBM - Tuned 1.6103 1.3662 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000

THử lại lần nữa với tham số:
RBMtuned = RBMAlgorithm(hiddenDim = 500, learningRate = 0.0001)

Nhận thấy là điểm số có tăng lên:
Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
RBM - Tuned 1.6139 1.3635 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000

Thử tăng hiddenDim: RBMtuned = RBMAlgorithm(hiddenDim = 5000, learningRate = 0.00001)

Algorithm RMSE MAE HR cHR ARHR Coverage Diversity Novelty  
RBM - Tuned 1.5904 1.3488 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000

Kết quả có tăng lên đôi chút nhưng không đáng kể, có vẻ như đã tối ưu hết mức và cần tập data lớn hơn để hiệu quả.

### Tập 10k record

Cho chạy dò tổ hợp tham số:
param_grid = {'hiddenDim': [200, 100, 50, 150, 70], 'learningRate': [0.5, 0.01, 0.001, 0.002, 0.0001]}
