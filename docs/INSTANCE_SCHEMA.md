# Tree identity and attributes

A biological tree can have several observations. Each observation can have several components or derived models.
The fields below keep these relationships clear. An unknown value remains `null`.

| Field | Definition |
|---|---|
| instance_id | Stable key for a source release, plot, and source tree ID. |
| biological_tree_id | Identity of one biological tree, when evidence supports this identity. |
| observation_id | Identity of one measurement event or scan group. |
| native_tree_id / plot_id | IDs from the source. |
| source_file / member | Source file and archive member. |
| modality / acquisition_date / leaf_state | Measurement method, date, and leaf condition. |
| species / taxonomy_source | Source species label and naming reference. |
| unit / CRS / transform | Units, coordinate reference system, and explicit coordinate transform. |
| component | Whole tree, leaf, wood, stem, or shoot. |
| geometry_kind | Point cloud, image-based mesh, QSM, graph, or 3DGS. |
| completeness | Boundary flag, occlusion, missing parts, and foreign points. |
| measured_attributes | Field measurements with units and methods. |
| derived_attributes | Estimates with methods, parameters, and parent observations. |
| rights / references | Data license, paper, and source documentation. |
| qa_status | Review state with a reason and evidence. |

## Geometry checks

1. Check units and axis directions.
2. Check the tree base, stem, top, and crown boundary.
3. Check occlusion and points from other trees.
4. Check species labels and component labels.
5. Check model units and transforms against the source observation.
6. Record each transformation as a derived version.

An instance ID does not establish complete geometry. A QSM describes reconstructed wood.
Missing leaves cannot be recorded as measured leaves. Display colors are not measured spectra.
