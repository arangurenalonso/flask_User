from app import app
from flask import render_template, request
from flask_login import login_required
from app.product.productController import ProductController
from app.product.productForm import ProductForm
from app.product.productModel import Product
from app.category.categoryModel import Category


@app.route('/products')
@login_required
def products():
    page = request.args.get('page', type=int, default=1)
    search = request.args.get('search', type=str, default='')
    category = request.args.get('category', type=int, default='')
    categories = Category.query.filter_by(status = 1).all
    controller = ProductController()
    products = controller.index(page=page, search=search, category = category)
    return render_template('views/products/index.html', 
                        title='Productos', data=products, search=search, categories = categories, category = category)


@app.route('/products/create', methods=['GET', 'POST'])
@login_required
def products_create():
    form = ProductForm()
    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category_id.choices = categories
    if form.validate_on_submit():
        controller = ProductController()
        return controller.create(form)
    return render_template('views/products/form/create.html', title='Productos', form=form)


@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
@login_required
def products_update(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category_id.choices = categories
    if form.validate_on_submit():
        controller = ProductController()
        return controller.update(form)
    return render_template('views/products/form/update.html', title='Productos', form=form)


@app.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def products_delete(id):
    controller = ProductController()
    return controller.delete(id)

