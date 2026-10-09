# Figure methods

## Scope

The figures show six examples from four sources. The example members come from an earlier source atlas.
They are not a random sample of trees. They do not establish the distribution of shapes in each source.

Tropical and Quebec examples use named members. The BCI example uses the leaf and wood pair with the smallest combined file size.
Wytham examples use the two PLY files closest to 1,500,000 bytes. File-size selection can favor scans with fewer points.
This publication includes only examples with explicit source data licenses.

All four sources state CC BY 4.0 for their data. The figures have the same license.
Source credits are in [Attribution](../assets/figures/ATTRIBUTION.md).

## Source examples

| Source | Example | Source points | Points shown | Vertical extent (m) |
|---|---|---:|---:|---:|
| Tropical leaf-wood | dro_033_pc | 81,830 | 14,000 | 22.562 |
| BCI | TETPANA_6185 | 125,797 | 14,000 | 24.829 |
| Quebec | DUC0001-01_53 | 282,809 | 14,000 | 20.756 |
| Quebec | DUC0001-01_54 | 266,407 | 14,000 | 14.336 |
| Wytham | wytham_winter_8224 | 125,146 | 14,000 | 22.760 |
| Wytham | wytham_winter_8084 | 125,157 | 14,000 | 7.486 |

The vertical extent is the maximum z minus the minimum z for finite source points.
It is not an independent field measurement of tree height.
Source members are listed in [figure_examples.json](../catalog/figure_examples.json).

## Sampling and coordinates

Each source member was read in full. Points with non-finite coordinates were excluded.
The examples use uniform random sampling without replacement. The generator is NumPy `default_rng`, with seed 42.
Each view contains at most 14,000 points. Display coordinates are rounded to 0.001 m.

The x and y origins move to their bounding-box centers. The z origin moves to the lowest source point.
No rotation, shape fitting, or size normalization is applied to the coordinates.
Units are interpreted as metres from the source. No independent scale calibration is made.

The views use a camera elevation of 18 degrees and an azimuth of minus 60 degrees.
The displayed x and y ranges are minus 7 m to plus 7 m. The z range is 0 m to 28 m.
Each axis uses the same physical unit length. All selected source extents fit inside these ranges.

## Colors

Tropical leaf-wood provides point labels: 0 for leaf and 1 for wood.
The BCI example combines the matching leaf and wood files. Its classes come from file membership.
These two label sources are different. The figures use green for leaf and brown for wood.

The Quebec and Wytham figures use one color scale for z above the lowest point.
The scale is 0 m to 28 m. The colors do not show material reflectance or species.

## Vertical profiles

The profiles use all finite source points, before display sampling.
Each example has 20 equal bins between its minimum and maximum z.
Each bin value is its point count divided by the example point count, expressed as a percentage.

Bin thickness differs between examples because their vertical extents differ. The curves are point proportions, not physical point density.
The profiles do not measure leaf area density, biomass, or sensor accuracy.
