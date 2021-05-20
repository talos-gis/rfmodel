#pragma once

#define TIREM3_EXPORT __declspec(dllimport)

TIREM3_EXPORT
void CalcTiremLoss(float tx_antenna_height, float rx_antenna_height, float frequency,
                   int num_profile_points, const float * profile_elevation, const float * profile_distance, int extension,
                   float refractivity, float conductivity, float permittivity, float humidity,
                   const char * polarization, char * version, char * propagation_mode,
                   float * fresnel_clearance, float * total_loss, float * free_space_loss,
                   const char * activation_key);