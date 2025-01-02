const CACHE_KEY = 'product_cache';
const CACHE_DURATION = 24 * 60 * 60 * 1000;

function setCacheItem(key, data) {
    const cacheData = {
        timestamp: Date.now(),
        data: data
    };
    localStorage.setItem(`${CACHE_KEY}_${key}`, JSON.stringify(cacheData));
}

function getCacheItem(key) {
    const cached = localStorage.getItem(`${CACHE_KEY}_${key}`);

    const cachedData = JSON.parse(cached);

    return cachedData.data;
}