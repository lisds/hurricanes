test = {
  'name': 'Question example_aces',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ivan_2004_ace'
          >>> 'ivan_2004_ace' in vars()
          True
          >>> # You haven't changed the value for 'ivan_2004_ace'
          >>> # from its initial state (of ...)
          >>> ivan_2004_ace is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You need to set the value for 'isabel_2003_ace'
          >>> 'isabel_2003_ace' in vars()
          True
          >>> # You haven't changed the value for 'isabel_2003_ace'
          >>> # from its initial state (of ...)
          >>> isabel_2003_ace is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(ivan_2004_ace) == 70
          True
          >>> round(isabel_2003_ace) == 63
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
