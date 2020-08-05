def ichimoku(price_objs, period=9):
    prdf = price_objs
    # Tenkan-sen (Conversion Line): (short-period high + short-period low)/2))
    period9_high = prdf.rolling(window=period).max()
    period9_low = prdf.rolling(window=period).min()
    tenkan_sen = (period9_high + period9_low) / 2

    # Kijun-sen (Base Line): (med-period high + med-period low)/2))
    period26_high = prdf.rolling(window=(3*period-1)).max()
    period26_low =prdf.rolling(window=(3*period-1)).min()
    kijun_sen = (period26_high + period26_low) / 2

    # Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))
    senkou_span_a = ((tenkan_sen + kijun_sen) / 2).shift(3*period)

    # Senkou Span B (Leading Span B): (long-period high + long-period low)/2))
    period52_high = prdf.rolling(window=(6*period)-2).max()
    period52_low = prdf.rolling(window=(6*period)-2).min()
    senkou_span_b = ((period52_high + period52_low) / 2).shift(3*period)

    # The most current closing price plotted 22 time periods behind (optional)
    chikou_span = prdf.shift(-22)  # 22 according to investopedia

    return tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span
    
    
