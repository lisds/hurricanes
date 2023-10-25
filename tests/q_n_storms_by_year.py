test = {
  'name': 'Question n_storms_by_year',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'n_storms_by_year'
          >>> 'n_storms_by_year' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'n_storms_by_year'
          >>> # from its initial state (of ...)
          >>> n_storms_by_year is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(n_storms_by_year, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },

      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
