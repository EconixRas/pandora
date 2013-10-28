
/*
 * Copyright (c) 2012
 * COMPUTER APPLICATIONS IN SCIENCE & ENGINEERING
 * BARCELONA SUPERCOMPUTING CENTRE - CENTRO NACIONAL DE SUPERCOMPUTACIÓN
 * http://www.bsc.es

 * This file is part of Pandora Library. This library is free software; 
 * you can redistribute it and/or modify it under the terms of the
 * GNU General Public License as published by the Free Software Foundation;
 * either version 3.0 of the License, or (at your option) any later version.
 * 
 * Pandora is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this library.  If not, see <http://www.gnu.org/licenses/>.
 * 
 */

#include <Simulation.hxx>
#ifdef PANDORAMPI
#include <mpi.h>
#endif
#include <iostream>
#include <Exceptions.hxx>
#include <cmath>
#include <sstream>

namespace Engine
{


Simulation::Simulation( const Point2D<int> & size, const int & numSteps, const int & serializerResolution ) : _id(-1), _numTasks(1), _size(size), _numSteps(numSteps), _localRasterSize(0,0), _serializerResolution(serializerResolution)
{
}

Simulation::~Simulation()
{
}

void Simulation::init()
{
#ifdef PANDORAMPI
	MPI_Comm_size(MPI_COMM_WORLD, &_numTasks);
	MPI_Comm_rank(MPI_COMM_WORLD,&_id);	
	std::cout << "simulation: " << _id << " of: " << _numTasks << " initialized" << std::endl;
#else
	_id = 0;
	_numTasks = 1;
#endif	
	_localRasterSize._x = _size._x/sqrt(_numTasks);
	_localRasterSize._y = _size._y/sqrt(_numTasks);
	if(_localRasterSize._x%2!=0 || _localRasterSize._y%2!=0)
	{
		// TODO fix when matrix not squared
		std::stringstream oss;
		oss << "Simulation::init - local raster width and height: " << _localRasterSize << " must be divisible by 2";
		throw Exception(oss.str());
	}
}
	
const int & Simulation::getId() const
{
	return _id;
}

const int & Simulation::getNumTasks() const
{
	return _numTasks;
}

const Point2D<int> & Simulation::getSize() const
{
	return _size;
}

const int & Simulation::getNumSteps() const
{
	return _numSteps;
}

const Point2D<int> & Simulation::getLocalRasterSize() const
{
	return _localRasterSize;
}

const int & Simulation::getSerializerResolution() const
{
	return _serializerResolution;
}

} // namespace Engine

