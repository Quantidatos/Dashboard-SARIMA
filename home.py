import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Inicio', title='SARIMA | Home')

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([
            html.H3(['Aplicativo web para optimizar modelos SARIMA']),
            html.P([html.B(['Luis E. Cayatopa-Rivera'])], className='par'),
            html.P([html.B(['Doctorado en Economía: Técnicas para el manejo de Series de tiempo'])], className='par'),
            html.P([html.B(['Universidad Nacional Mayor de San Marcos'])], className='par')
        ], width=12, className='row-titles')
    ]),
    # Guidelines
    dbc.Row([
        dbc.Col([], width = 2),
        dbc.Col([
            html.P([html.B('1) Conjunto de datos'),html.Br(),
                    'El data set analizado es la Producción Nacional de Ajo de Perú (en Miles de Toneladas). 2007.01-2024.08'], className='guide'),
            html.P([html.B('2) Aplicar transformaciones para hacer que los datos sean estacionarios'),html.Br(),
                    'Las herramientas disponibles son: Logaritmo y diferenciación, el gráfico de Box-Cox y la prueba de Dickey Fuller Aumentado.',html.Br(),
                    'Una vez que los datos sean estacionarios, verificar los gráficos ACF y PACF para obtener parámetros de modelo adecuados.'], className='guide'),
            html.P([html.B('3) Realizar una búsqueda en la cuadrícula del modelo SARIMA.'),html.Br(),
                    'Elejir la división de entrenamiento-prueba y proporcione rangos de origen a destino para cualquier parámetro.'
                    'El componente de estacionalidad del modelo se puede excluir dejando todos los parámetros de la derecha en 0.',html.Br(),
                    'Se muestran los 10 modelos con mejor desempeño (según el criterio AIC).'], className='guide'),
            html.P([html.B('4) Configurar el modelo final'),html.Br(),
                    'Se sugieren los parámetros para el mejor modelo del paso anterior.',html.Br(),
                    'El modelo SARIMA con los parámetros de entrada se ajusta automáticamente a los datos de entrenamiento; se realizan predicciones para los datos de entrenamiento y de prueba.',html.Br(),
                    'Se presenta el análisis ACF y PACF de los residuos del modelo.'], className='guide')
        ], width = 8),
        dbc.Col([], width = 2)
    ])
])