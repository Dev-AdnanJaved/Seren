"""
=============================================================
  CRYPTO PUMP SCANNER v5 — COMPLETE CONFIG
  Every setting, every API key, every toggle is here.
  Set keys you have, leave others empty → bot auto-skips.
=============================================================
"""

# ═════════════════════════════════════════════
#  TELEGRAM  (required)
# ═════════════════════════════════════════════
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"   # from @BotFather on Telegram
TELEGRAM_CHAT_ID   = "YOUR_CHAT_ID_HERE"     # your chat ID from /getUpdates

# ═════════════════════════════════════════════
#  FREE SOURCES — no key needed, always enabled
# ═════════════════════════════════════════════

# Binance Futures public API (price, OHLCV, OI, funding, L/S, order book)
BINANCE_API_KEY    = ""   # optional — only for private endpoints
BINANCE_API_SECRET = ""

# Bybit public API (OI, funding, L/S, order book — no key needed)
ENABLE_BYBIT_FETCH  = True

# OKX public API (OI, funding, L/S, order book — no key needed)
ENABLE_OKX_FETCH    = True

# Bitget public API (OI, funding, order book — no key needed)
ENABLE_BITGET_FETCH = True

# Alternative.me Fear & Greed Index (completely free, no key)
ENABLE_FEAR_GREED   = True

# CoinGecko (market cap, supply, community, news — free, rate limited)
ENABLE_COINGECKO_NEWS = True

# Google Trends via pytrends (free, no key — pip install pytrends)
# Set False if hitting rate limits
ENABLE_GOOGLE_TRENDS = False

# BTC market context filter (free — uses Binance API)
# Suppresses alt alerts when BTC is crashing hard
ENABLE_BTC_FILTER         = True
BTC_CRASH_THRESHOLD_PCT   = -3.0    # BTC 4h change below this = crashing
BTC_CRASH_SCORE_PENALTY   = 4       # subtract from score when BTC crashing
BTC_SIDEWAYS_BONUS        = 1       # add to score when BTC is calm/sideways

# Telegram activity approximation (free — CoinGecko + CryptoCompare)
ENABLE_TELEGRAM_ACTIVITY  = True

# ═════════════════════════════════════════════
#  FREE WITH ACCOUNT — get free key, no payment
# ═════════════════════════════════════════════

# CoinGlass — best aggregated OI, liquidations, L/S across ALL exchanges
# Free key at: https://coinglass.com/pricing (Starter = free)
# Without key → falls back to manual per-exchange aggregation
ENABLE_COINGLASS  = True
COINGLASS_API_KEY = ""

# Coinalyze — aggregated OI, funding, CVD, liquidation heatmap
# Free key at: https://coinalyze.net/settings/api
ENABLE_COINALYZE  = True
COINALYZE_API_KEY = ""

# CryptoPanic — REMOVED: they ended free tier in 2024 (now paid only)
# News is now handled by CryptoCompare (free, no key needed)
# If you have a CryptoPanic paid key you can re-enable in news_fetcher.py
ENABLE_CRYPTOPANIC    = False   # disabled — free tier removed
CRYPTOPANIC_API_KEY   = ""
NEWS_LOOKBACK_HOURS   = 24      # look at news from last N hours

# CoinMarketCal — token unlock / event calendar
# Free key at: https://developers.coinmarketcal.com/
ENABLE_COINMARKETCAL  = False
COINMARKETCAL_API_KEY = ""

# LunarCrush — social volume, galaxy score, alt rank
# Free tier: 10k credits/month at https://lunarcrush.com/developers
# Fallback: CoinGecko community data (free)
ENABLE_LUNARCRUSH  = False
LUNARCRUSH_API_KEY = ""

# ═════════════════════════════════════════════
#  PAID SOURCES — professional grade data
#  Leave ENABLE = False and key = "" to skip
# ═════════════════════════════════════════════

# Glassnode — on-chain: new addresses, exchange flows, active addresses
# Plans from ~$39/month at https://studio.glassnode.com/
ENABLE_GLASSNODE  = False
GLASSNODE_API_KEY = ""

# CryptoQuant — exchange inflow/outflow, netflow
# Plans from ~$29/month at https://cryptoquant.com/
ENABLE_CRYPTOQUANT    = False
CRYPTOQUANT_API_KEY   = ""

# Nansen — smart money / labeled whale wallet tracking
# Plans from ~$150/month at https://www.nansen.ai/
ENABLE_NANSEN    = False
NANSEN_API_KEY   = ""

# Arkham Intelligence — labeled entity on-chain tracking
# Plans from ~$50/month at https://platform.arkhamintelligence.com/
ENABLE_ARKHAM    = False
ARKHAM_API_KEY   = ""

# Twitter/X API v2 — tweet count and mention spikes
# Basic plan: $100/month at https://developer.twitter.com/
# Note: LunarCrush covers this on free tier — use that first
ENABLE_TWITTER        = False
TWITTER_BEARER_TOKEN  = ""

# Santiment — social dominance, dev activity, whale tx count
# Plans from ~$49/month at https://app.santiment.net/
ENABLE_SANTIMENT    = False
SANTIMENT_API_KEY   = ""

# Hyblock Capital — liquidation heatmap (where liq clusters are)
# Plans from ~$30/month at https://app.hyblock.io/
ENABLE_HYBLOCK    = False
HYBLOCK_API_KEY   = ""

# ═════════════════════════════════════════════
#  SCANNER SETTINGS
# ═════════════════════════════════════════════
SCAN_INTERVAL_MINUTES  = 15            # scan every 15 minutes
SCAN_QUOTE_ASSET       = "USDT"

# ── Filters applied to ALL ~600 Binance Futures coins ──
MIN_VOLUME_USDT        = 500_000       # skip coins with <$500K daily volume
                                       # (lower = more coins, catches hidden gems)
MAX_MARKET_CAP_USD     = 500_000_000   # <$500M market cap only (small caps)
                                       # Set to 0 to disable cap filter (scan all)

# ── Signal thresholds ──
VOLUME_SPIKE_THRESHOLD = 2.5           # vol must be 2.5x 7d average
OI_CHANGE_THRESHOLD    = 8.0           # OI must be up >=8% in 24h
FUNDING_RATE_MAX       = 0.0           # funding <= this = squeeze setup
LONG_SHORT_RATIO_MAX   = 1.0           # ratio < 1 = more shorts than longs

# ── Two-tier scanning system ──────────────────────────────────────
#
# TIER 1 — PRIORITY (scanned every single cycle, always):
#   Top N coins by pre-score. Never skipped.
PRIORITY_SCAN_LIMIT    = 60
#
# TIER 2 — ROTATION (round-robin, all coins covered over time):
#   Remaining coins in rotating batches. No coin permanently skipped.
ROTATION_BATCH_SIZE    = 150           # 60+150=210 coins per scan → full coverage every 2 scans (30 min)
#
# Total per scan = 60 + 150 = 210 coins
#
# ── Parallel execution ────────────────────────────────────────────
#
# How many coins to scan simultaneously (threads).
# Each coin's internal API calls are ALSO parallelised (6 threads each).
#
# With COIN_PARALLEL_WORKERS=5:
#   5 coins × 2.5s = ~3-4 min scan time (was 18 min sequential)
#
# Higher = faster scans BUT more simultaneous connections to APIs.
# Too high may trigger rate limits on some exchanges.
# Recommended: 3-6 depending on your server's network speed.
COIN_PARALLEL_WORKERS  = 10           # 210 coins / 10 workers = ~6-7 min per scan
#
# Minimum pre-score to run slow social/news API calls.
# Coins below this skip community/telegram/news (saves ~1s per coin).
# These calls only matter for coins that might actually alert.
# Set to 0 to run social for all coins (slower but complete).
SOCIAL_MIN_PRESCORE    = 2
#
# Timing estimate with defaults:
#   100 coins / 5 workers = 20 batches × 2.5s = ~50s
#   Plus overhead = ~2-3 minutes total per scan
#
# Full rotation with 300 eligible coins:
#   240 in rotation ÷ 40 per scan = 6 scans = 3 hours full coverage
#
# ── Pump Scanner defaults ────────────────────────────────────────
PUMPS_DEFAULT_LOOKBACK  = 7     # /pumps default: last N days
PUMPS_DEFAULT_MIN_PCT   = 50    # /pumps default: minimum pump %
PUMPS_MIN_VOLUME_USDT   = 100_000  # minimum 24h volume to include in /pumps scan

# Legacy (kept for other modules)
DEEP_SCAN_LIMIT        = 210
TOP_N_COINS            = 210

# ═════════════════════════════════════════════
#  SCORING WEIGHTS
#  Tune these after backtesting your CSV data.
#  Higher number = signal matters more.
# ═════════════════════════════════════════════
SCORE_WEIGHTS = {
    # ── Core futures signals (2 pts each) ──────────────────
    "volume_spike":        2,   # today vol > 2.5x 7d average
    "oi_rising":           2,   # OI up >=8% across all exchanges
    "negative_funding":    2,   # funding negative (shorts paying)
    "short_heavy":         2,   # L/S ratio < 1 (more shorts)
    "cvd_divergence":      2,   # CVD rising + flat price = hidden buying
    "chart_pattern":       2,   # falling wedge / bull flag / cup&handle etc

    # ── Technical signals (1 pt each) ──────────────────────
    "bb_squeeze":          1,   # Bollinger Bands tightening
    "low_atr":             1,   # low volatility = calm before storm
    "higher_lows":         1,   # rising lows + sideways price
    "far_from_ath":        1,   # >40% below ATH = room to run

    # ── Market structure (1 pt each) ───────────────────────
    "small_market_cap":    1,   # market cap < $500M
    "high_leverage":       1,   # OI/MC ratio > 0.3
    "negative_basis":      1,   # futures below spot price
    "whales_short":        1,   # top trader L/S < 1
    "low_float":           1,   # circulating supply < 30% of total

    # ── Sentiment (1 pt each) ──────────────────────────────
    "social_spike":        1,   # social volume spike (LunarCrush)
    "google_trends":       1,   # Google search spike
    "fear_greed_low":      1,   # Fear & Greed index <= 35
    "news_catalyst":       1,   # positive news / listing announcement
    "twitter_spike":       1,   # tweet count spike (Twitter API or LunarCrush)

    # ── Order book (1 pt each) ─────────────────────────────
    "exchange_outflow":    1,   # taker buy pressure > 55%
    "buy_wall":            1,   # large buy wall across exchanges
    "ob_imbalance":        1,   # bid > ask by >20% across exchanges
    "arb_signal":          1,   # cross-exchange spread = price move imminent

    # ── On-chain / paid signals (1 pt each) ────────────────
    "smart_money_buying":  1,   # Nansen smart money net buying
    "whale_accumulating":  1,   # Arkham / Glassnode exchange outflow
    "liq_magnet_above":    1,   # Hyblock: liq cluster above price = magnet
    "btc_sideways_bonus":  1,   # BTC calm = good for alt pumps
}

# ═════════════════════════════════════════════
#  AVOID / PENALTY SIGNALS
# ═════════════════════════════════════════════
PENALTY_UNLOCK_RISK    = 3    # token unlock soon
PENALTY_BTC_CRASH      = 4    # BTC crashing = all alts suffer
PENALTY_NEGATIVE_NEWS  = 3    # hack/exploit/rug news detected
PENALTY_ALREADY_PUMPED = 2    # already up >50% in 7 days
PENALTY_HIGH_FUNDING   = 2    # funding too positive = overleveraged longs

# ═════════════════════════════════════════════
#  ALERT SETTINGS
# ═════════════════════════════════════════════
ALERT_MIN_SCORE       = 10    # raised from 6 to cut structural noise
ALERT_COOLDOWN_HOURS  = 72    # same coin can only alert once every 3 days

# ── Momentum Gate ─────────────────────────────────────────────────
# Prevents alerting coins scoring only from structural/universal signals.
# (fear&greed + BTC sideways + falling_wedge = 4-5 pts FREE on every coin)
# When True: at least one real momentum signal must fire before alerting.
REQUIRE_MOMENTUM_SIGNAL = True   # vol_spike/oi_rising/cvd_divergence/etc
MOMENTUM_BYPASS_SCORE   = 20     # very high scores bypass the gate

ALERT_MAX_PER_SCAN    = 10    # max alerts per scan cycle

# ── Signal Tracker (15-day paper trade monitoring) ─────────────────
# Signals scoring >= PAPER_TRADE_SCORE get tracked for 15 days
# Bot monitors price and notifies at pump milestones
# All signals stored in data/signal_tracker/ as JSON
PAPER_TRADE_SCORE     = 13    # track signals with score >= this
SIGNAL_MONITOR_DAYS   = 15    # monitor each signal for N days
PUMP_NOTIFY_THRESHOLDS  = [10, 20, 30, 50, 75, 100]  # notify on % pump
DUMP_NOTIFY_THRESHOLDS  = [-10, -20, -30]              # notify on % dump
ALERT_MAX_PER_SCAN    = 10    # max alerts per scan cycle

# ═════════════════════════════════════════════
#  DATA LOGGING
# ═════════════════════════════════════════════
ENABLE_CSV_LOGGING   = True
CSV_LOG_PATH         = "data/scan_log.csv"
ENABLE_PUMP_TRACKING = True
PUMP_TRACK_DAYS      = 10    # check back N days later to see if it pumped

# ═════════════════════════════════════════════
#  NETWORK
# ═════════════════════════════════════════════
REQUEST_TIMEOUT  = 10    # seconds per request
RATE_LIMIT_DELAY = 0.1   # seconds between API calls (parallel mode handles rate limits)
