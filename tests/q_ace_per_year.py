test = {
  'name': 'Question ace_per_year',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ace_per_year'
          >>> 'ace_per_year' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'ace_per_year'
          >>> # from its initial state (of ...)
          >>> ace_per_year is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(ace_per_year, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> len(ace_per_year) == 172
          True
          >>> np.all(ace_per_year.index == np.arange(1851, 2023))
          True
          >>> np.all(ace_per_year.iloc[:4] == [36.24, 73.28, 76.49, 31])
          True
          >>> np.all(ace_per_year.iloc[-4:] == [132.2025, 180.3725, 145.5575,
          ...                                   110.45])
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
