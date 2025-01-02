const catalogElement = document.getElementById('catalog');
const productsContainer = document.getElementById('products-container');
const productDetailsElement = document.getElementById('product-details');

function createProductCard(product) {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.innerHTML = `
        <img src="${product.image}" alt="${product.name}" class="product-image">
        <h2 class="product-title">${product.title}</h2>
        <p class="product-price">${product.price} GBP</p>
    `
    card.addEventListener('click', () => showProductDetail(product.id));
    return card;
}

async function displayProducts() {
    const products = await fetchProducts();
    productsContainer.innerHTML = '';
    products.forEach(product => {
        productsContainer.appendChild(createProductCard(product));
    });
}

async function showProductDetail(productId) {
    const product = await fetchProductsById(productId);
    if (!product) {
        return
    }

    catalogElement.classList.add('hidden');
    productDetailsElement.classList.add('active');
    productDetailsElement.innerHTML = `
        <button onclick="showCatalog()">Back to Catalog</button>
        <div class="product-detail">
            <img src="${product.image}" alt="${product.name}" class="product-image">
            <h2 class="product-title">${product.title}</h2>
            <p class="product-price">${product.price} GBP</p>
            <p>Category: ${product.category}</p>
            <p>Rating: ${product.rating.rate}</p>
        </div>
    `
}

function showCatalog() {
    catalogElement.classList.remove('hidden');
    productDetailsElement.classList.remove('active');
}
