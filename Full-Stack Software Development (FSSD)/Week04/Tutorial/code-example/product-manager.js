const API_URL = 'https://fakestoreapi.com';

async function fetchProducts() {
    const cachedProducts = getCacheItem('all');
    if (cachedProducts) {
        return cachedProducts;
    }

    try {
        const response = await fetch(`${API_URL}/products`);
        if (!response.ok) {
            throw new Error('Failed to fetch products');
        }
        const products = await response.json();
        setCacheItem('all', products);
        return products;
    } catch (error) {
        console.error('Error fetching products', error);
    }
}

async function fetchProductsById(id) {
    const cachedProduct = getCacheItem(`product_${id}`);
    if (cachedProduct) {
        return cachedProduct;
    }

    try {
        const response = await fetch(`${API_URL}/products/${id}`);
        if (!response.ok) {
            throw new Error('Failed to fetch product');
        }
        const product = await response.json();
        setCacheItem(`product_${id}`, product);
        return product;
    } catch (error) {
        console.error('Error fetching product', error);
    }
}