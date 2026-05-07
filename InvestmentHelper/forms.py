from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

from InvestmentHelper.utils.choices import (
    AssetCountryChoices,
    AssetSectorChoices,
    AssetTypeChoices,
    RequiredRiskLevelChoices,
    RiskLevelChoices,
)


class AssetFilterForm(FlaskForm):
    asset_type = SelectField('Investment type', choices=AssetTypeChoices.choices())
    country = SelectField('Country', choices=AssetCountryChoices.choices())
    sector = SelectField('Sector', choices=AssetSectorChoices.choices())
    risk_level = SelectField('Maximum risk', choices=RiskLevelChoices.choices())
    search_pattern = StringField('Search pattern', validators=[Optional()])
    submit = SubmitField('Filter')


class RecommendationForm(AssetFilterForm):
    risk_level = SelectField('Maximum risk', choices=RequiredRiskLevelChoices.choices(), validators=[DataRequired()])
    amount = FloatField(
        'Amount to invest',
        validators=[DataRequired(), NumberRange(min=100)],
        render_kw=dict(placeholder='30000'),
    )
    submit = SubmitField('Generate suggestion')
