import dash_core_components as dcc
import dash_html_components as html

layout2 = html.Div([
    #preloader
    # html.Div([
    #     html.Div(className='loader')
    # ],
    # id='preloader'
    # ),

    #main wrapper
    html.Div([
        #main header
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.A([
                                html.Img(
                                    src='assets/img/logo2.png',
                                    alt='logo'
                                )
                            ],
                            href='#'
                            )
                        ],
                        className='logo')
                    ],
                    className='col-md-3'
                    ),
                    #profile info
                    html.Div([
                        html.Div([
                            html.Ul([
                                html.Li([
                                    html.I(className='ti-fullscreen')
                                ],
                                id='full-view'
                                ),
                                html.Li([
                                    html.I(className='ti-zoom-out')
                                ],
                                id='full-view-exit')
                            ],
                            className='notification-area')
                        ],
                        className='d-md-inline-block d-block mr-md-4'
                        ),
                        html.Div([
                            html.Div([
                                html.Img(
                                    className='avatar user-thumb',
                                    src='assets/img/chris.png',
                                    alt='avatar'
                                ),
                                html.H4([
                                    'Chriss Desy',
                                    html.I(className='fa fa-angle-down')
                                ],
                                className='user-name dropdown-toggle',
                                **{'data-toggle':'dropdown'}
                                ),
                                html.Div([
                                    html.A(
                                        'Log Out',
                                        className='dropdown-item',
                                        href='#'
                                    )
                                ],
                                className='dropdown-menu')
                            ],
                            className='user-profile m-0')
                        ],
                        className='clearfix d-md-inline-block d-block')
                    ],
                    className='col-md-9 clearfix text-right')
                ],
                className='row align-items-center')
            ],
            className='container')
        ],
        className='mainheader-area'
        ),
        #header area ... navigation
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Nav([
                                html.Ul([
                                    html.Li([
                                        html.A([
                                            html.I(className='ti-dashboard'),
                                            html.Span('home')
                                        ],
                                        href='javascript:void(0)'
                                        ),
                                        html.Ul([
                                            html.Li([
                                                html.A(
                                                    'Dashboard',
                                                    href=''
                                                    )
                                            ])
                                        ],
                                        className='submenu')
                                    ]),
                                    html.Li([
                                        html.A([
                                            html.I(className='ti-slice'),
                                            html.Span('Add new...')
                                        ],
                                        href='javascript:void(0)'
                                        ),
                                        html.Ul([
                                            html.Li([
                                                html.A(
                                                    'CSV',
                                                    href=''
                                                )
                                            ]),
                                            html.Li([
                                                html.A(
                                                    'others...',
                                                    href=''
                                                )
                                            ])
                                        ],
                                        className='submenu')
                                    ]),
                                    html.Li([
                                        html.A([
                                            html.I(className='ti-pie-chart'),
                                            html.Span('Charts')
                                        ],
                                        href='javascript:void(0)'
                                        ),
                                        html.Ul([
                                            html.Li([
                                                html.A(
                                                    'Bar Chart',
                                                    href=''
                                                )
                                            ]),
                                            html.Li([
                                                html.A(
                                                    'Line Chart',
                                                    href=''
                                                )
                                            ]),
                                            html.Li([
                                                html.A(
                                                    'Pie Chart',
                                                    href=''
                                                )
                                            ])
                                        ],
                                        className='submenu')
                                    ]),
                                    html.Li([
                                        html.A([
                                            html.I(className='fa fa-table'),
                                            html.Span('Tables')
                                        ],
                                        href='javascript:void(0)'
                                        ),
                                        html.Ul([
                                            html.Li([
                                                html.A(
                                                    'Basic Table',
                                                    href=''
                                                )
                                            ]),
                                            html.Li([
                                                html.A(
                                                    'Data Table',
                                                    href=''
                                                )
                                            ])
                                        ],
                                        className='submenu')
                                    ]),
                                    html.Li([
                                        html.A([
                                            html.I(className='ti-map-alt'),
                                            html.Span('Maps')
                                        ],
                                        href='')
                                    ])
                                ],
                                id='nav_menu')
                            ])
                        ],
                        className='horizontal-menu')
                    ],
                    className='col-lg-9 d-none d-lg-block'
                    ),
                    #mobile menu
                    html.Div([
                        html.Div(id='mobile_menu')
                    ],
                    className='col-12 d-block d-lg-none')
                ],
                className='row align-items-center')
            ],
            className='container')
        ],
        className='header-area header-bottom'
        ),

        #main content area
        html.Div([
            html.Div([
                html.Div([
                    #Facts area
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                'TB Notifications'
                                            ],
                                            className='seofct-icon'),
                                            html.H2('2,315')
                                        ],
                                        className='p-4 d-flex justify-content-between align-items-center')
                                    ],
                                    className='seo-fact sbg1')
                                ],
                                className='card')
                            ],
                            className='col-md-6 mt-5 mb-3'
                            ),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                'Completed Treatments'
                                            ],
                                            className='seofct-icon'),
                                            html.H2('3,984')
                                        ],
                                        className='p-4 d-flex justify-content-between align-items-center')
                                    ],
                                    className='seo-fact sbg2')
                                ],
                                className='card')
                            ],
                            className='col-md-6 mt-5 mb-3'
                            ),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                'On Treatment'
                                            ],
                                            className='seofct-icon'),
                                            html.H2('1,234')
                                        ],
                                        className='p-4 d-flex justify-content-between align-items-center')
                                    ],
                                    className='seo-fact sbg4')
                                ],
                                className='card')
                            ],
                            className='col-md-6'
                            ),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                'Deaths'
                                            ],
                                            className='seofct-icon'),
                                            html.H2('567')
                                        ],
                                        className='p-4 d-flex justify-content-between align-items-center')
                                    ],
                                    className='seo-fact sbg3')
                                ],
                                className='card')
                            ],
                            className='col-md-6 mb-3 mb-lg-0'
                            )

                        ],
                        className='row',
                        style={
                            'alignItems': 'center'
                        })
                    ],
                    className='col-lg-8'
                    ),
                    
                    #Bar chart
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H4(
                                    'Bar Charts',
                                    className='header-title'
                                ),
                                html.Div(
                                    'Graph Here...',
                                    style={'height':'245px'}
                                    )
                            ],
                            className='card-body pb-0')
                        ],
                        className='card')
                    ],
                    className='col-lg-4 mt-5'
                    ),

                    #Line Chart
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H4(
                                    'Line Chart',
                                    className='header-title'
                                ),
                                html.H6('Graph Here...')
                            ],
                            className='card-body')
                        ],
                        className='card')
                    ],
                    className='col-lg-8 mt-5'
                    ),

                    #Pie Chart
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H4(
                                    'Pie Chart',
                                    className='header-title'
                                ),
                                html.H6('Graph Here...')
                            ],
                            className='card-body')
                        ],
                        className='card')
                    ],
                    className='col-lg-4 mt-5'
                    ),

                    #Scatter Plot
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H4(
                                    'Scatter Plot Chart',
                                    className='header-title'
                                ),
                                html.Div('Graph Here...')
                            ],
                            className='card-body')
                        ],
                        className='card')
                    ],
                    className='col-xl-8 col-lg-8 mt-5'
                    ),

                    #map
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H4(
                                    'Map',
                                    className='header-title'
                                ),
                                html.Div('Graph Here...')
                            ],
                            className='card-body')
                        ],
                        className='card')
                    ],
                    className='col-lg-5 mt-5')

                ],
                className='row')
            ],
            className='container')
        ],
        className='main-content-inner'),

        #footer
        html.Footer([
            html.Div([
                html.P([
                    '© Copyright 2019. All right reserved. ',
                    html.A(
                        '#teammulaga',
                        href=''
                    )
                ])
            ],
            className='footer-area')
        ])
    ],
    className='horizontal-main-wrapper')
],
className='body-bg')