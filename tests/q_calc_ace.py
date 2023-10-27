test = {
  'name': 'Question calc_ace',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> calc_ace(vmax_vals)
          4.91
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> res = calc_ace(np.array([10, 20, 30]))
          >>> np.isclose(res, 0.14)
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
