from flask import Blueprint, render_template, request

from InvestmentHelper.forms import AssetFilterForm, RecommendationForm
from InvestmentHelper.queries import create_recommendation, get_assets_by_filters

investment = Blueprint('investment', __name__)


@investment.route("/")
@investment.route("/home")
def home():
    return render_template('pages/home.html')


@investment.route("/about")
def about():
    return render_template('pages/about.html')


@investment.route("/assets", methods=['GET', 'POST'])
def assets():
    form = AssetFilterForm()
    assets_list = []
    searched = request.method == 'POST'
    if request.method == 'POST' and form.validate_on_submit():
        assets_list = get_assets_by_filters(
            asset_type=form.asset_type.data,
            country=form.country.data,
            sector=form.sector.data,
            risk_level=form.risk_level.data,
            search_pattern=form.search_pattern.data,
        )
    return render_template('pages/assets.html', form=form, assets=assets_list, searched=searched)


@investment.route("/recommendations", methods=['GET', 'POST'])
def recommendations():
    form = RecommendationForm()
    recommendations_list = []
    submitted = request.method == 'POST'
    if request.method == 'POST' and form.validate_on_submit():
        recommendations_list = create_recommendation(form.data)
    total_allocated = sum(float(item.allocated_amount) for item in recommendations_list)
    for item in recommendations_list:
        item.allocation_percent = (float(item.allocated_amount) / total_allocated * 100) if total_allocated else 0
    average_risk = (
        sum(int(item.risk_level) for item in recommendations_list) / len(recommendations_list)
        if recommendations_list else 0
    )
    return render_template(
        'pages/recommendations.html',
        form=form,
        recommendations=recommendations_list,
        submitted=submitted,
        total_allocated=total_allocated,
        average_risk=average_risk,
    )
