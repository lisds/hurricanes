test = {
  'name': 'Question hu_tracks_per_year',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'hu_tracks_per_year'
          >>> 'hu_tracks_per_year' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'hu_tracks_per_year'
          >>> # from its initial state (of ...)
          >>> hu_tracks_per_year is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(hu_tracks_per_year, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You might or might not have dropped the 0 tracks years.
          >>> len(hu_tracks_per_year) in (170, 172)
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
