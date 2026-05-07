from flask import Blueprint, render_template, request

from InvestmentHelper.forms import AssetFilterForm, RecommendationForm
from InvestmentHelper.queries import create_recommendation, get_assets_by_filters

Investment = Blueprint('Investment', __name__)


@Investment.route("/")
@Investment.route("/home")
def home():
    return render_template('pages/home.html')


@Investment.route("/about")
def about():
    return render_template('pages/about.html')


@Investment.route("/assets", methods=['GET', 'POST'])
def assets():
    form = AssetFilterForm()
    assets_list = []
    if request.method == 'POST' and form.validate_on_submit():
        assets_list = get_assets_by_filters(
            asset_type=form.asset_type.data,
            country=form.country.data,
            sector=form.sector.data,
            risk_level=form.risk_level.data,
            search_pattern=form.search_pattern.data,
        )
    return render_template('pages/assets.html', form=form, assets=assets_list)


@Investment.route("/recommendations", methods=['GET', 'POST'])
def recommendations():
    form = RecommendationForm()
    recommendations_list = []
    if request.method == 'POST' and form.validate_on_submit():
        recommendations_list = create_recommendation(form.data)
    return render_template('pages/recommendations.html', form=form, recommendations=recommendations_list)
