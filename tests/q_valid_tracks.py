test = {
  'name': 'Question valid_tracks',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'valid_tracks'
          >>> 'valid_tracks' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'valid_tracks'
          >>> # from its initial state (of ...)
          >>> valid_tracks is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(valid_tracks, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> ((valid_tracks['Datetime'].dt.hour % 6) == 0).all()
          True
          >>> (valid_tracks['Datetime'].dt.minute == 0).all()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(valid_tracks)
          34931
          >>> valid_tracks[ws_col].sum()
          2176500
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
