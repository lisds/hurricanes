test = {
  'name': 'Question dt_strings',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'dt_strings'
          >>> 'dt_strings' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'dt_strings'
          >>> # from its initial state (of ...)
          >>> dt_strings is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(dt_strings, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dt_strings.iloc[0] == '18510625 0000'
          True
          >>> dt_strings.iloc[1] == '18510625 0600'
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
